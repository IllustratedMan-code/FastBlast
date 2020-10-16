
library(treemap) 								# treemap package by Martijn Tennekes

# Set the working directory if necessary
# setwd("C:/Users/username/workingdir");

# --------------------------------------------------------------------------
# Here is your data from REVIGO. Scroll down for plot configuration options.


RevigoTreemap <- function(name){
    stuff <- read.csv(name)
    stuff$plot_X <- NULL
    stuff$plot_Y <- NULL
    stuff$plot_size <- NULL

    stuff$frequency <- substr(stuff$frequency, 1, nchar(stuff$frequency)-1)
    names(stuff)[names(stuff) =="frequency"] <- "freqInDbPercent"
    stuff$log10.p.value <- abs(stuff$log10.p.value)
    names(stuff)[names(stuff) =="log10.p.value"] <- "abslog10pvalue"
    names(stuff)

    name <- substr(name, 1, nchar(name) - 4)




    stuff$abslog10pvalue <- as.numeric( as.character(stuff$abslog10pvalue) );
    stuff$freqInDbPercent <- as.numeric( as.character(stuff$freqInDbPercent) );
    stuff$uniqueness <- as.numeric( as.character(stuff$uniqueness) );
    stuff$dispensability <- as.numeric( as.character(stuff$dispensability) );

    # by default, outputs to a PDF file
    pdf( file=paste("/home/david/Documents/blast/Blastfiles/outputfiles/Genelists/profileddata/RevigoData/RevigoTreemaps/", name, ".pdf", sep=""), width=16, height=9 ) # width and height are in inches

    # check the tmPlot command documentation for all possible parameters - there are a lot more
    treemap(
        stuff,
        index = c("representative","description"),
        vSize = "abslog10pvalue",
        type = "categorical",
        vColor = "description",
        title = "REVIGO Gene Ontology treemap",
        inflate.labels = FALSE,      # set this to TRUE for space-filling group labels - good for posters
        lowerbound.cex.labels = 0,   # try to draw as many labels as possible (still, some small squares may not get a label)
        bg.labels = "#CCCCCCAA",     # define background color of group labels
                                                        # "#CCCCCC00" is fully transparent, "#CCCCCCAA" is semi-transparent grey, NA is opaque
        position.legend = "none"
    )

    dev.off()
}
setwd("/home/david/Documents/blast/Blastfiles/outputfiles/Genelists/profileddata/RevigoData")
list.files(pattern="*.csv")
for(i in list.files(pattern="*.csv")){
    RevigoTreemap(i)
}
