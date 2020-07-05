--- 
title:"introduction to R syntax"
output:html_notebook
---
```{r}
25 * 4 + 9 /3
```
print('Sunday')

full_name <- 'Abam'

greet_message <- 'Hello ther!'
print(greet_message)

greet_message <- 'Sunday Abam'
print(greet_message)


name <- 'Ruby'

spring_months <- c("March", "April","May","June")
print(spring_months)


phone <- c(+234,080,6932,5391)

#conditional Statement
message <- "I changed based on a condition"
if(TRUE){
    message <- "I execute this when true!"
}else{
    message <- 'I execute this when false!'
}
print(message)
#Comparison Operators
56 >= 129  # False
56 != 129  #True

#Logical Operators
Season <- "should i pack an umbrella"
weather <- "cloudy"
high_chance_of_rain <- TRUE

if(weather == "cloudy" & high_chance_of_rain){
    message <- "pack an umbrella"
}else{
    message <- "No need for umbrella"
}
print(message)

#Calling a function
data <- c(120,34,54,67,120)
unique_vals <- unique(data)
print(unique)

solution <- sqrt(49)
print(solution)


round_up <- floor(3.14)
print(round_up)

round_down <- ceiling(3.14)
print(round_down)


#importing package
{r}
#library
library(dlpyr)
library(readr)




