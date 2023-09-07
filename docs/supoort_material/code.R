library(pdftools)
library(tidyverse)

# if (!require("pdftools")) install.packages("pdftools")
# if (!require("tidyverse")) install.packages("tidyverse")
# if (!require("tidyverse")) install.packages("openxlsx")
lectura<- pdftools::pdf_text("m2020.pdf")

lectura[38]


class(lectura)

df=
  as.data.frame(lectura) %>% 
  mutate(detecta=str_detect(lectura, "Título")) %>% 
  filter(detecta==T) %>% 
  mutate(oeae=map(.x=lectura, ~emi_function(.x)))

emi<-lectura[36]

oe=as.data.frame(str_locate_all(emi, "\r\n"))

dim(oe)[1]

oe[2,1]



openxlsx::write.xlsx(df, "emilio.xlsx")

str_sub(emi,39,608)

texto=emi


texto=df$lectura[[37]]
emi_function<- function(texto){
  
  donde_esta<- as.data.frame(str_locate_all(texto, "\r\n"))
  dimen=dim(donde_esta)[1]
  
  inicio=donde_esta[2,1]
  final=donde_esta[dimen-3,1]
  
  textof=str_sub(texto, start = inicio, end = final)
  
  return(textof)
  
  
  
}

df$oeae[[36]]
