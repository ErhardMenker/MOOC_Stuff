# set the working directory
setwd("C:/Data/Analytics_Studies/R/Data_Science_Specialization/Getting&Cleaning_Data")

# Question 1

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
download.file(fileUrl, "./question1.csv") # download the file to the WD in question1.csv
DF <- read.csv("./question1.csv") # read this into a data frame
sum(DF$VAL==24, na.rm=TRUE) # sum the amount of $1,000,000 homes, removing NAs

# Question 3 (In Development)

require(openxlsx) # use this instead of xlsx package because of java compatability issues

# manually read in since there are corruption issues
# read in this xlsx file with the given row/column constraints
dat <- openxlsx::read.xlsx("./question3.xlsx", rows = 18:23, cols = 7:15)
sum(dat$Zip*dat$Ext,na.rm=T)

# Question 4

require(XML)

fileUrl <- "http://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml"
# place online xml in a handler called doc
doc <- XML::xmlTreeParse(fileUrl, useInternal=TRUE)
# extract the set of zip code nodes
zipcode_nodes <- getNodeSet(doc, "/response//zipcode")
# convert these zip code nodes into a character vector type
zipcode_nodes2 <- sapply(zipcode_nodes, xmlValue)
# sum the character vectors where the value is "21231"
sum(sapply(zipcode_nodes2, function(elem) elem == "21231"))

# Question 5

require(data.table)

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv"
download.file(fileUrl, "./question5.csv")
# read the CSV into a data table
DT <- fread("./question5.csv")

profiler <- function(operation) {
    start.time <- Sys.time()
    operation
    end.time <- Sys.time()
    return(end.time - start.time)
}

profiler(mean(DT$pwgtp15,by=DT$SEX))
profiler(sapply(split(DT$pwgtp15,DT$SEX),mean))
profiler(DT[,mean(pwgtp15),by=SEX])
profiler(mean(DT[DT$SEX==1,]$pwgtp15); mean(DT[DT$SEX==2,]$pwgtp15))
profiler(tapply(DT$pwgtp15,DT$SEX,mean))
profiler(rowMeans(DT)[DT$SEX==1]; rowMeans(DT)[DT$SEX==2])
