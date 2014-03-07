activ <- read.csv('/data/italia/src/just_one_month.dat')


weekday_levels <- c("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
activ$weekday <- factor(activ$weekday, levels=weekday_levels)

summary(activ)

levels(activ$type)

library(ggplot2)

# Plot Italy curves
activ2 <- activ[activ$type %in% c('Italy'), ]
ggplot(activ2, aes(x=hour)) + 
  #geom_line(aes(y=smsin_m, group=date, color=weekday), size=0.8) + 
  geom_smooth(aes(y=callin_m, group=date, color=weekday), size=1.5, method='loess', span=0.5, se=FALSE) + 
  #facet_grid(type ~ .)  +
  #theme_bw() +
  theme(axis.title.y=element_blank(), axis.ticks.y=element_blank(), axis.text.y=element_blank())


# Plot Inter curves
activ2 <- activ[activ$type %in% c('inter', 'Italy'), ]
ggplot(activ2, aes(x=hour)) + 
  #geom_line(aes(y=smsin_m, group=date, color=weekday), size=0.8) + 
  geom_smooth(aes(y=callin_m, group=date, color=weekday), size=1.5, method='loess', span=0.5, se=FALSE) + 
  facet_grid(type ~ .)  +
  theme_bw() +
  theme(axis.title.y=element_blank(), axis.ticks.y=element_blank(), axis.text.y=element_blank())



# Austria vs China vs Italia
activ2 <- activ[activ$type %in% c('Poland', 'China', 'United States', 'Morocco', 'Czech Republic'), ]
ggplot(activ2, aes(x=hour)) + 
  #geom_line(aes(y=smsin_m, group=date, color=weekday), size=0.8) + 
  geom_smooth(aes(y=callin_m+callout_m, group=date, color=weekday), size=1.5, method='loess', span=0.5, se=FALSE) + 
  facet_grid(type ~ weekday)  +
  theme_bw() +
  theme(axis.title.y=element_blank(), axis.ticks.y=element_blank(), axis.text.y=element_blank())
