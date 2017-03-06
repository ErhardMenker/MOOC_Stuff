setwd("C:/Data/Analytics_Studies/R/Data_Science_Specialization/Getting&Cleaning_Data")

# Question 1

# create a folder for disk files if does not exist
if(!file.exists("./quiz3files")){dir.create("./quiz3files")}
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv", 
              destfile="./quiz3files/question1.csv")
DF1 <- read.csv("./quiz3files/question1.csv")

# create a logical vector of households > than 10 acres with more than $10,000 worth of ag product
agricultureLogical <- DF1$ACR == 3 & DF1$AGS == 6
# find out which rows of the DF have TRUE logicals
which(agricultureLogical)[1:3]

# Question 2

require(jpeg)
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fjeff.jpg", 
              destfile="./quiz3files/question2.jpg", mode = "wb")
# use readJPEG() to place this jpg file in an img handle
img <- readJPEG(source="./quiz3files/question2.jpg", native=TRUE)
quantile(img, probs=c(0.3, 0.8))

# Questions 3 - 5

# download the 2 different files
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv",
              destfile="./quiz3files/question3a.csv")
download.file(url="https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv",
              destfile="./quiz3files/question3b.csv")
# read the files in to handles
DF3A <- read.csv("./quiz3files/question3a.csv", skip=4, nrows=190)
DF3B <- read.csv("./quiz3files/question3b.csv")

# merge the two data sets based on the country codes, and sort in descending order by GDP
require(dplyr); require(plyr)
DF3A <- dplyr::rename(DF3A, CountryCode=X, RankRGDP=X.1, CountryLong=X.3)
DF3A$RGDP <- as.numeric(gsub(",", "", DF3A$RankRGDP)) # remove the strings from the factor... 
# ...and make numeric
DF3 <- plyr::arrange(plyr::join(DF3A, DF3B), desc(RankRGDP))

# Question 3
paste("common countries: ", nrow(DF3))
paste("13th row:", DF3$CountryLong[13])

# Question 4
paste("average GDP rank for High Income countries in OECD:", 
      mean(DF3$RankRGDP[DF3$Income.Group == "High income: OECD"], na.rm=TRUE))
paste("average GDP rank for High Income countries not in OECD:", 
      mean(DF3$RankRGDP[DF3$Income.Group == "High income: nonOECD"], na.rm=TRUE))

# Question 5
require(Hmisc)
# create a quantile of the RankRGDP and place it in the rgdpGroups column in DF3 as a categorical var
DF3$rgdpGroups <- Hmisc::cut2(DF3$RankRGDP, g=5)
# create a table of the different rgdp groups based on income (e.g. how many of the countries in...
# each rgdp quantile fall in the different income groups?)
inc_tab <- table(DF3$rgdpGroups, DF3$Income.Group)
inc_tab




