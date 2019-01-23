v1 <- dnorm(0.5, mean=0, sd=1)
v2 <- dnorm(0.3, mean=3, sd=4)
v3<- dnorm(0.2, mean=-2, sd=0.5)
x<-sum(v1,v2,v3)

plot(function (x)
{ sapply(x, FUN = function(v) { sum(v1,v2,v3)}) 
}, -10, 10)


