library(frbs)
library(raster)
setwd("/home/anurag/Documents/IIRS/Module_8/Fuzzy Lab/")
etm<-stack('pt_image.bsq')
df<-as.data.frame(etm)
tbl<-read.table('pt_roi.txt',comment.char = ";",col.names=c('ID','X','Y','B1','B2','B3','B4','B5','B6'))
tbl['class']=c(rep(1,960),rep(2,665),rep(3,489),rep(4,639),rep(5,159),rep(6,103))

tblShuffled <- tbl[sample(nrow(tbl)), ]

range.data.input <- matrix(c(0, 255, 0, 255, 0, 255, 0, 255,0,255,0,255), nrow=2)
TrainData = tblShuffled[1:1500, 4:10]
TestData = tblShuffled[1501:nrow(tblShuffled), 4:9]
ValidationData= matrix(tblShuffled[1501:nrow(tblShuffled), 10], ncol=1)

range.data.input = matrix(c(0, 255, 0, 255, 0, 255, 0, 255,0,255,0,255), nrow=2)
method.type <- "FRBCS.CHI" #used to change the error from 34% to 9%
control = list(num.labels = 6, type.mf = "TRAPEZOID", type.tnorm = "MIN",
                type.snorm = "MAX", type.implication.func = "ZADEH",
                name = "sim-0") # changed to TRAPEZOID to bring error down from 76% to 9%
#control = list(num.labels = 6, type.mf = "TRIANGLE")

object = frbs.learn(TrainData, range.data.input, method.type, control)
pred = predict(object, TestData)
err = 100 * sum(pred != ValidationData) / length(pred)
#err  #used formminimisation of error

res.test = predict(object, df) #THIS TAKES A HELL OF A LOT OF TIME. HOW TO PARALLELIZE THIS PROBLEM?
etm_res=matrix(res.test,ncol=512) #loading the class values in a matrix.

cls<-raster(etm) # creating raster
extent(cls)<-extent(etm)
cls[]<-etm_res[] #loading values in the raster

for(i in seq(1,2)){   #checking if values are correctly loaded in the raster or not
  for(j in seq(1,512)){
    err.sum=sum(etm_res[i,j] != cls[i,j])
  }
}

plot(cls)  # finally plotting the raster