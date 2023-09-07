rm(list=ls())
library(readxl)
library(dplyr)
library(readxl)
library(tidytext)
library(stringr)
library(ggplot2)
library(wordcloud)
library(syuzhet)
library(tm)


custom_stop_words <- bind_rows(stop_words,
                               data_frame(word = tm::stopwords("spanish"),
                                          lexicon = "custom"))
m100 <- read_excel("m100.xlsx")

tidy_cuentos <- m100 %>%
  unnest_tokens(word, Cuento)


tidy_cuentos <- tidy_cuentos %>%
  anti_join(custom_stop_words)

conteo<-tidy_cuentos %>%
  count(word, sort = TRUE) 

tidy_cuentos %>%
  count(word, sort = TRUE) %>%
  filter(n > 40) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(n, word)) +
  geom_col() +
  labs(y = NULL)

tidy_cuentos %>%
  count(word) %>%
  with(wordcloud(word, n, max.words = 1000))

tidy_cuentos<-as.character(tidy_cuentos)
cuento_df <- get_nrc_sentiment(tidy_cuentos, lang="spanish")
head(cuento_df)

texto_palabras <- get_tokens(m100)
head(texto_palabras)
sentimientos_df <- get_nrc_sentiment(texto_palabras, lang="spanish")
head(sentimientos_df)


barplot(
  colSums(prop.table(sentimientos_df[, 1:8])),
  space = 0.2,
  horiz = FALSE,
  las = 1,
  cex.names = 0.7,
  col = brewer.pal(n = 8, name = "Set3"),
  main = "Medellín en 100 palabras",
  sub = "Análisis realizado por un topa",
  xlab="emociones", ylab = NULL)

barplot(colSums(prop.table(sentimientos_df[, 1:8])))


palabras_tristeza <- texto_palabras[sentimientos_df$sadness> 0]
palabras_tristeza_orden <- sort(table(unlist(palabras_tristeza)), decreasing = TRUE)
head(palabras_tristeza_orden, n = 12)
length(palabras_tristeza_orden)

palabras_confianza <- texto_palabras[sentimientos_df$trust> 0]
palabras_confianza_orden <- sort(table(unlist(palabras_confianza)), decreasing = TRUE)
head(palabras_confianza_orden, n = 12)
length(palabras_confianza_orden)


nube_emociones_vector <- c(
  paste(texto_palabras[sentimientos_df$sadness> 0], collapse = " "),
  paste(texto_palabras[sentimientos_df$joy > 0], collapse = " "),
  paste(texto_palabras[sentimientos_df$anger > 0], collapse = " "),
  paste(texto_palabras[sentimientos_df$fear > 0], collapse = " "))

nube_emociones_vector <- iconv(nube_emociones_vector, "latin1", "UTF-8")

nube_corpus <- Corpus(VectorSource(nube_emociones_vector))

nube_tdm <- TermDocumentMatrix(nube_corpus)
nube_tdm <- as.matrix(nube_tdm)
head(nube_tdm)

colnames(nube_tdm) <- c('tristeza', 'felicidad', 'enfado', 'confianza')
head(nube_tdm)


set.seed(757) # puede ser cualquier número
comparison.cloud(nube_tdm, random.order = FALSE,
                 colors = c("green", "red", "orange", "blue"),
                 title.size = 1, max.words = 50, scale = c(2.5, 1), rot.per = 0.4)