library(ggplot2) 
library(plotly)

data_titanic <- read.csv("train.csv", header = TRUE, sep = ",", quote = "\"", dec = ".", fill = TRUE, comment.char = "")

View(head(data_titanic))

df <- as.data.frame(data_titanic)

df$Name <- NULL
df$Cabin <- NULL
df$Ticket <- NULL
df$PassengerId <- NULL

View(df)

plot(data_titanic$Survived,data_titanic$PassengerId)

hist(df$Pclass[df$Survived==0])
hist(df$Pclass[df$Survived==1])

sum(is.na(df$Survived))
sum(is.na(df$Pclass))
sum(is.na(df$Sex))
sum(is.na(df$Age))
sum(is.na(df$SibSp))
sum(is.na(df$Parch))
sum(is.na(df$Fare))
sum(is.null(df$Embarked))

df$Sex<-as.numeric(df$Sex)
df$Embarked<-as.numeric(df$Embarked)

View(df)
