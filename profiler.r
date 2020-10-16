library(gprofiler2)


files <- list.files(pattern="*.csv")

setwd("/home/david/Documents/blast/Blastfiles/outputfiles/Genelists")
for (file in files){
    q <- list(read.csv(file))
    query <- gost(query = q, organism = "iscapularis")
    write.table(cbind(query$result$term_id, query$result$p_value), file=paste("profileddata/", file, sep=""),quote=FALSE, row.names=FALSE, col.names=FALSE)
}