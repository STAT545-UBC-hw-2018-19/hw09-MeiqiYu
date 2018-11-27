library(tidyverse)
library(stringr)

words <- readLines("words.txt")
words <- gsub("[[:punct:]]", "", words)

letters_list <- rep(0, length(letters))


for (i in words) {
	
	first <- str_to_upper(str_sub(i, start = 1, end = 1))
	number <-  as.numeric(match(first,LETTERS))
	
	letters_list[number] <- letters_list[number] + 1
	
}

first_table <- data.frame(letter = LETTERS, count = letters_list)

write.table(first_table,"first_letter.tsv",
						sep = "\t", row.names = FALSE, quote = FALSE)

