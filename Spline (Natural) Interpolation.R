setwd('D:/DATAAAAA')

# Read ground water level Data
df <- read.csv('GWL- malwathu oya 2017 - 2019.csv')

# Time Sequence
ger <- data.frame(DATE= as.Date(c("2017-01-01", "2017-04-01", "2017-07-01", "2017-10-01",
                                  "2018-01-01", "2018-04-01", "2018-07-01", "2018-10-01",
                                  "2019-01-01", "2019-04-01", "2019-07-01", "2019-10-01")),
                                  VALUE= t(df[10,6:17]))

# Create ground water level with time sequence
DateSeq <- seq(ger$DATE[1],tail(ger$DATE,1),by="1 month")


gerMonthly <- data.frame(DATE=DateSeq, water_depth=round(spline(ger, method="natural",
                                                        xout=DateSeq)$y, digits = 2))

# write data into csv
write.csv(gerMonthly, 'depth.csv')

#plot 
plot(gerMonthly$water_depth, type='l', col = "blue", xlab = "Time (month)", ylab = "Water Depth (m)",
    main = "Water Depth Interpolated (Spline)")
