# Databricks notebook source
# MAGIC %md 
# MAGIC 
# MAGIC # Eksploracyjna analiza danych (EDA) z wykorzystaniem PySparka

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Eksploracyjna analiza danych jest jedną z najważniejszych części każdego procedu analizy. Bez prawidłowo opisanych danych, a  następnie oczyszczonych - proces analizy nie może zakończyć się sukcesem.
# MAGIC 
# MAGIC Można ją podzielić na kilka stadiów:
# MAGIC 
# MAGIC 1. Eksploracja dancyh:
# MAGIC 
# MAGIC     1. Przegląd typów danych
# MAGIC     2. Przegląd rozkładu wartości, w tym wartości odstających
# MAGIC     3. Przegląd wartości brakujących lub błędów systematyczncyh
# MAGIC 
# MAGIC 2. Oczyszczanie danych:
# MAGIC     1. Uzupełnianie wartości brakujących
# MAGIC     2. Obsługa wartości odstających w zbirze.
# MAGIC   

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC # Analiza wartości brakujących

# COMMAND ----------

df_miss = spark.createDataFrame([ (1, 143.5, 5.6, 28,
'M', 100000),
(2, 167.2, 5.4, 45, 'M', None),
(3, None , 5.2, None, None, None),
(4, 144.5, 5.9, 33, 'M', None),
(5, 133.2, 5.7, 54, 'F', None),
(6, 124.1, 5.2, None, 'F', None),
(7, 129.2, 5.3, 42, 'M', 76000),
], ['id', 'weight', 'height', 'age', 'gender', 'income'])

# COMMAND ----------

df_miss.show()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Wyszukiwanie obserwacji z brakującymi wartościami - przejście na **RDD** i analiza, których elementów brakuje.
# MAGIC 
# MAGIC Podstawową operacją będzie zliczenie brakujących wartości w wierszach.
# MAGIC 
# MAGIC Struktura kodu:
# MAGIC 
# MAGIC 
# MAGIC ```{python}
# MAGIC 
# MAGIC data_frame.rdd.map(lambda row: ANALIZA)
# MAGIC 
# MAGIC ```

# COMMAND ----------

# Analizujemy ilośc brakujących wartości w każdym wieszu - suma brakujących pól

df_miss.rdd.map(
	lambda row: (row['id'], sum([c == None for c in row]))
).collect()

# Oczekiwany wynik: pary uporządkowane: (id_wiersza, SUMA wartości brakujących), np.: (1, 10), (2, 0)


# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Analiza procentowa udziału wartości brakujących w całym zbiorze - analiza wg. każdej kolumny po kolei.
# MAGIC 
# MAGIC Składnia polecenia:
# MAGIC 
# MAGIC ```{python}
# MAGIC 
# MAGIC import pyspark.sql.functions as fn
# MAGIC 
# MAGIC data_frame.agg(
# MAGIC   (1- (fn.count( KOLUMNA )/fn.count('*')))
# MAGIC ).show()
# MAGIC 
# MAGIC ```

# COMMAND ----------

import pyspark.sql.functions as fn

df_miss.where('id == 3').show()


# Oczekiwany wynik - procentowy udział wartości brakujących w całym zbiorze

# COMMAND ----------

# To samo dla wielu kolumn - iteracja po wszystkich wartościach

df_miss.agg(*[
 (1 - (fn.count(c)/fn.count('*'))).alias(c + '_missing')
  for c in df_miss.columns
]).show()

# Oczekiwany wynik - procentowy udział wartości brakujących w każdej kolumnie


# COMMAND ----------

# Wiersze, w których brakuje więcej niż X wartości można po prostu opuścić - usunąć ze zbioru danych. Poleceniem dropna(threshold=X)

df_miss_with_income = df_miss.dropna(thresh=3)
df_miss_with_income.show()

# Oczekiwany wynik - zbiór danych bez wierszy, w których brakuje co najmniej 3 wartości

# COMMAND ----------

# Usunięcie kolumny income, ze względu na zbyt duży procent obserwacji brakujących

df_miss_no_income = df_miss_with_income.select([ c for c in df_miss.columns if c != 'income'])
df_miss_no_income.show()


# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Usuwanie wartości brakujących nie jest najlepszym sposobem. Zazwyczaj można jakoś je uzupełnić. Są na to co najmniej dwa sposoby:
# MAGIC 
# MAGIC 1. Można użyć stałej wartości (tzw. sposób wartości "magicznej") - np. -1 albo 0.
# MAGIC 2. Można użyć jakiejś wartości charakterystycznej dla danej kolumny -np. średniej/mediany itp.

# COMMAND ----------

# Sposób 1 - wstawianie stałej wartości

means = df_miss_no_income.agg(
     *[fn.mean(c).alias(c)
          for c in df_miss_no_income.columns if c != 'gender']
).toPandas().to_dict('records')[0]

means['age'] = '0'
df_miss_no_income.fillna(means).show()


# Oczekiwany wynik - zbiór danych, gdzie brakujące wartości uzupełniono zerami

# COMMAND ----------

# Sposób 2 - użycie średniej

# Krok 1 - znajdujemy średnią wartości dla każdej kolumny po kolei

means2 = df_miss_no_income.agg(
     *[fn.mean(c).alias(c)
          for c in df_miss_no_income.columns if c != 'gender'])

means2.show()


# Oczekiwany wynik - zbiór danych, gdzie wyliczono średnią wartośc dla każdej kolumny (z wyjątkiem 'gender')

# COMMAND ----------

# Krok 2 -zamiana zbioru danych średnich na słownik 

means_dict = means2.toPandas().to_dict('records')[0]
means_dict

# Oczekiwany wynik - słownik, gdzie dla każdej kolumny umieszczono średnią wartośc. Dla kolumny gender -wstawic '??'

# COMMAND ----------

# Krok 3 - wykorzystanie słownika w funkcji fillna

df_miss_no_income.fillna(means_dict).show()

# Oczekiwany wynik - zbiór danych uzupełniony średnimi z poprzedniego punktu

