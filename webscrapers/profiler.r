library(gprofiler2)
outputdir <- "/home/david/Documents/BenoitLab/RNA-seq/Gprofiler/"
inputdir <- "/home/david/Documents/BenoitLab/NewBlast/Output/"
setwd(inputdir)
files <- list.files(pattern = "*.csv")

for (file in files) {
  q <- list(read.csv(file))
  query <- gost(query = q, organism = "iscapularis")
  write.table(cbind(query$result$term_id, query$result$p_value), file = paste(outputdir, file, sep = ""), quote = FALSE, row.names = FALSE, col.names = FALSE)
}