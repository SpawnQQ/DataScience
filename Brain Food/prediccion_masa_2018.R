# Version de R 3.4.4

if('forecast' %in% rownames(installed.packages()) == FALSE) {install.packages('forecast')}
if('prophet' %in% rownames(installed.packages()) == FALSE) {install.packages('prophet')}
if('dplyr' %in% rownames(installed.packages()) == FALSE) {install.packages('dplyr')}
if('RODBC' %in% rownames(installed.packages()) == FALSE) {install.packages('RODBC')}
library(forecast)
library(RODBC)
library(prophet)
library(dplyr)

#######################################################################################
#                              Preparamos los datos                                   #
#######################################################################################

timeseries <- read.csv('Consumo Gas Region Magallanes.csv',sep=';')
paste(timeseries$Año,timeseries$Mes,timeseries$Dia, collapse="-")

timeseries$periodo <- apply( timeseries[ , c( 'Año' , 'Mes' , 'Dia' ) ] , 1 , paste , collapse = "-" )
timeseries$periodo <- as.Date(timeseries$periodo, "%Y-%m-%d")

# timeseries <- timeseries[timeseries$periodo >= '1996-01-01',]

#######################################################################################
#                              Datos por periodo semanal                              #
#######################################################################################

consumo_semanal <- read.csv('consumo_semanal.csv',sep=';')
consumo_semanal$periodo <- as.Date(consumo_semanal$periodo, "%Y-%m-%d")

#######################################################################################
#                           Datos por periodo mensual                                 #
#######################################################################################

consumo_mensual <- read.csv('consumo_mensual.csv',sep=';')
consumo_mensual$periodo <- as.Date(consumo_mensual$periodo, "%Y-%m-%d")

#######################################################################################
#                             Contemplamos los feriados                               #
#######################################################################################

feriados <- data_frame(
  holiday = 'feriado',
  ds = timeseries[timeseries$Feriado == 1,]$periodo,
  lower_window = 0,
  upper_window = 1)

holidays <- bind_rows(feriados)

#######################################################################################
#                             Entrenamiento y predicción                              #
#######################################################################################

##### Modelo por dias

model <- prophet(data.frame(ds=timeseries$periodo, y=timeseries$Consumo), holidays = holidays,n.changepoints = 21)

futuro_days <- make_future_dataframe(model, periods = 7,freq = "days",include_history = FALSE)

forecast_days <- predict(model, futuro_days)
forecast_days <- forecast_days[,c('ds','yhat')]
colnames(forecast_days) <- c('periodo', 'prediccion_consumo')
forecast_days$prediccion_consumo <- as.integer(forecast_days$prediccion_consumo)
forecast_days$periodo <- as.character.Date(forecast_days$periodo)

df.cv <- cross_validation(model, initial = 1170, period = 180, horizon = 365, units = 'days')
head(df.cv)

df.p <- performance_metrics(df.cv)
head(df.p)

plot_cross_validation_metric(df.cv, metric = 'mape')

##### Modelo por semanas

model <- prophet(data.frame(ds=consumo_semanal$periodo, y=consumo_semanal$Consumo), n.changepoints = 21)

futuro_weeks <- make_future_dataframe(model, periods = 5,freq = "week",include_history = FALSE)

forecast_weeks <- predict(model, futuro_weeks)
forecast_weeks <- forecast_weeks[,c('ds','yhat')]
colnames(forecast_weeks) <- c('periodo', 'prediccion_consumo')
forecast_weeks$prediccion_consumo <- as.integer(forecast_weeks$prediccion_consumo)

df.cv2 <- cross_validation(model, initial = 167, period = 180, horizon = 365, units = 'days')
head(df.cv2)

df.p2 <- performance_metrics(df.cv2)
head(df.p2)

plot_cross_validation_metric(df.cv2, metric = 'mape')

##### Modelo por meses

model <- prophet(data.frame(ds=consumo_mensual$periodo, y=consumo_mensual$Consumo), n.changepoints = 21)

futuro_months <- make_future_dataframe(model, periods = 3,freq = "months",include_history = FALSE)

forecast_months <- predict(model, futuro_months)
forecast_months <- forecast_months[,c('ds','yhat')]
colnames(forecast_months) <- c('periodo', 'prediccion_consumo')
forecast_months$prediccion_consumo <- as.integer(forecast_months$prediccion_consumo)
forecast_months$periodo <- as.character.Date(forecast_months$periodo)

df.cv3 <- cross_validation(model, initial = 39, period = 180, horizon = 365, units = 'days')
head(df.cv3)

df.p3 <- performance_metrics(df.cv3)
head(df.p3)

plot_cross_validation_metric(df.cv3, metric = 'mape')
