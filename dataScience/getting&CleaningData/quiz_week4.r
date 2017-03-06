setwd("C:/Users/MENKEEX1/Desktop/Local_Projects/JHU/Getting_and_cleaning_data")

# Question 1

# download the data and place in variable name
if(!dir.exists("./data")) {dir.create("./data")}
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv", 
              destfile="./data/acs.csv")
ACS <- read.csv("./data/acs.csv")

ans1 <- strsplit(names(ACS), "wgtp")[123]
ans1

# Question 2-3 Pre-process
library(dplyr)

if(!dir.exists("./data")) {dir.create("./data")}
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv", 
              destfile="./data/gdp.csv")
GDP <- read.csv("./data/gdp.csv", skip=4)[1:190, c(1:2, 4:5)]
GDP <- dplyr::rename(GDP, "country short"=X, "rank"=X.1, "country long"=X.3, "2012 GDP"=X.4)

# Question 2
as.character(GDP$"2012 GDP")
ans2 <- mean(as.numeric(sapply(as.character(GDP$"2012 GDP"), function(x) gsub(",","",x))), na.rm=TRUE)
paste("the average GDP in 2012 for the countries is:", ans2, "dollars")

# Question 3
ans3 <- length(grep("^United", GDP$"country long"))
paste("there are", ans3, "countries starting with United")

# Question 4
library(plyr); library(dplyr)

if(!dir.exists("./data")) {dir.create("./data")}
# read in FGDP data
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv", 
              destfile="./data/fgdp.csv")
FGDP <- read.csv("./data/fgdp.csv", skip=2)
FGDP <- FGDP[3:nrow(FGDP), c(1:2, 4:5)] # drop the first and second row of NAs and the NA columns
FGDP <- dplyr::rename(FGDP, "CountryCode"=X, "Rank"=X.1, "CountryLong"=X.3, "2012GDP"=X.millions.of)

# read in educational data
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv",
              destfile="./data/educ.csv")
EDUC <- read.csv("./data/educ.csv")

# concatenate the two data frames using plyr
MRG <- plyr::join(FGDP, EDUC, by="CountryCode")
# count how many of the Special.Notes entries mention June
table(grepl("Fiscal year end: [Jj][Uu][Nn][Ee]", as.character(MRG$Special.Notes)))

# Question 5
library(quantmod)

amzn = getSymbols("AMZN",auto.assign=FALSE)
sampleTimes = index(amzn) # sampleTimes is a date vector

#find out how many dates are in 2012
sum(grepl("^2012", as.Date(sampleTimes, "%y")), na.rm=TRUE)

#find out how many dates are in Monday of 2012?
sum(grepl("Mon12", format(sampleTimes, "%a%y")))





