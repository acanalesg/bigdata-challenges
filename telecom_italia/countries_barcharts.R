library(ggplot2)


countries <- read.csv('/data/italia/src/paises_calls_one_month.csv')

summary(countries)

countries$call_ratio <- 1 - countries$sms_to_all
countries$outgoing_ratio <- 1 - countries$in_to_all

# Number of countries to show
num_c <- 40
text_size <- 10

countries[order(countries$importance, decreasing=T), ][,"country"]

countries_filtered <- countries[order(countries$importance, decreasing=T), ][1:num_c,]

# Plot countries with more activity
ggplot(countries_filtered, 
       aes(x=country, y=importance, fill=importance)) +
  geom_bar(stat = "identity", alpha=0.9, color="black") + 
  scale_fill_gradientn(colours=c("gold", "orange2", "red")) + theme_bw() + 
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5, size=text_size, color="black"), 
        axis.title.x=element_blank(),
        axis.title.y=element_blank()) 

# Plot countries with more activity
#ggplot(countries[order(countries$importance, decreasing=T), ][1:num_c,], aes(x=country, y=importance, fill=importance)) + 
#  geom_bar(stat = "identity", alpha=0.9, color="black") +
#  scale_fill_gradientn(colours=c("lightyellow", "orange", "red")) + theme_bw() + 
#  theme(axis.text.x=element_text(angle=50,hjust=1,vjust=1, size=18, color="black"), 
#        axis.title.x=element_blank(),
#        axis.title.y=element_blank()) 


# Plot Outgoing ratios: outgoing/(outgoing + incoming)
ggplot(countries_filtered, 
       aes(x=country, y=outgoing_ratio, fill=outgoing_ratio)) + 
  geom_bar(stat = "identity", alpha=0.9, color="black") +
  scale_fill_gradientn(colours=c("white", "lightgreen", "darkgreen")) + theme_bw() + 
  scale_y_continuous(limits = c(0, 1)) + 
  theme(axis.text.x=element_text(angle=50,hjust=1,vjust=1, size=text_size, color="black"), 
        axis.title.x=element_blank(),
        axis.title.y=element_blank()) 

# Plot call ratio: calls/(calls + sms)
ggplot(countries_filtered, 
       aes(x=country, y=call_ratio, fill=call_ratio)) + 
  geom_bar(stat = "identity", alpha=0.9, color="black") +
  scale_fill_gradientn(colours=c("white", "lightblue", "dodgerblue4")) + theme_bw() + 
  scale_y_continuous(limits = c(0, 1)) + 
  theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5, size=text_size, color="black"), 
        axis.title.x=element_blank(),
        axis.title.y=element_blank()) 

