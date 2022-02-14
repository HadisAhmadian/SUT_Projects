#-------------------------------
BiocManager::install(c("GEOquery","limma","pheatmap","ggplot2","gplots","reshape2","plyr"))
BiocManager::install(c("pheatmap"),force = TRUE)
BiocManager::install(c("GOexpress"),force = TRUE)
library(GEOquery)
library(limma)
library(umap)
library(pheatmap)
library(GOexpress)
library(ggplot2)
library(reshape2)
library(plyr)
#-------------------------------

curD <- "F:/uni/bio_prj"
setwd(curD)

series <- "GSE48558"
platform <- "GPL6244"
gset <- getGEO(series,GSEMatrix = TRUE, AnnotGPL = TRUE , destdir = "data/")
if (length(gset) > 1) idx <- grep(platform, attr(gset, "names")) else idx <- 1
gset <- gset[[idx]] 

class(gset)

gsms <- paste0("1111111111111XXXXXXXXXXXXXXXXXXXXXXXXXXX0XXX0XXXXX",
               "XXXXXXXXXXXXXXXXXX0X0XXX0X0000X0XX00XX00X0X0X0X0X0",
               "XXX0XXX0XXXXXXXXXXXXXXXXXXXXXXXXXXXXX0000000110111",
               "00000000000000000000")

sml <- strsplit(gsms, split="")[[1]]

# filter out excluded samples (marked as "X")
sel <- which(sml != "X")
sml <- sml[sel]
gset <- gset[ ,sel]



######gr
ex<-exprs(gset)
dim(ex)

max(ex)
min(ex)
pdf("output/boxplot.pdf",width = 15)
boxplot(ex)
dev.off()
#ex <- normalizeQuantiles(ex)
#exprs(gset)<- gset

pdf("output/heat.pdf",width = 15,height  = 15)
pheatmap(cor(ex))
dev.off()

#####################################################################################################################


pc <- prcomp(ex)
pdf("output/pc_comp.pdf",width = 15,height  = 15)
plot(pc)
dev.off()

pdf("output/ex_pc1_2.pdf",width = 15,height  = 15)
plot(pc$x[,1:2])
dev.off()


ex.scale<-t(scale(t(ex),scale=F))
pc <- prcomp(ex.scale)
pdf("output/pc_comp_scale.pdf",width = 15,height  = 15)
plot(pc)
dev.off()

pdf("output/scale_ex_pc1_2.pdf",width = 15,height  = 15)
plot(pc$x[,1:2])
dev.off()

#####################################################################################################################


gsms <- paste0("0000000000000XXXXXXXXXXXXXXXXXXXXXXXXXXX3XXX3XXXXX",
               "XXXXXXXXXXXXXXXXXX1X5XXX3X3441X5XX55XX55X1X5X1X5X2",
               "XXX2XXX2XXXXXXXXXXXXXXXXXXXXXXXXXXXXX3333333005000",
               "11111115444435555555")
sml <- strsplit(gsms, split="")[[1]]
sel <- which(sml != "X")
gr <- sml[sel]
gs <- factor(gr)
groups <- make.names(c("test","n_Bcell","n_CD34","n_gran","n_mono","n_tcell"))
levels(gs) <- groups


pcr <- data.frame(pc$rotation[,1:2], Group=gs)
pdf("output/PCA_samples.pdf",width = 15,height  = 15)
ggplot(pcr,aes(PC1,PC2,color=Group))+geom_point(size=5)
dev.off()


pdf("output/sample_corr.pdf",width = 15,height  = 15)
pheatmap(cor(t(pc$rotation[,1:5])),labels_row = gs, labels_col = gs)
dev.off()

#####################################################################################################################


gs<-factor(gs)
gset$group <- gs
design <- model.matrix(~group + 0, gset)
colnames(design) <- levels(gs)

head(design)

fit <- lmFit(gset, design)  # fit linear model

# set up contrasts of interest and recalculate model coefficients
cts <- paste("test", "n_CD34", sep="-")
cont.matrix <- makeContrasts(contrasts=cts, levels=design)
fit2 <- contrasts.fit(fit, cont.matrix)

# compute statistics and table of top significant genes
fit2 <- eBayes(fit2, 0.01)
tT <- topTable(fit2, adjust="fdr", sort.by="B", number=Inf)
head(tT)


tT <- subset(tT, select=c("Gene.symbol", "ID","adj.P.Val","logFC"))
write.table(tT, file="output/diff.txt", row.names=F, sep="\t",quote=F)



test.up <- subset(tT, logFC>1 & adj.P.Val<0.05)
test.up.gen <- unique(as.character( strsplit2(test.up$Gene.symbol,"///")))
write.table(test.up.gen, file="output/testUpGene.txt",quote=F, row.names = F,col.names = F)


test.down <- subset(tT, logFC<-1 & adj.P.Val<0.05)
test.down.gen <- unique(as.character( strsplit2(test.down$Gene.symbol,"///")))
write.table(test.down.gen, file="output/testDownGene.txt",quote=F, row.names = F,col.names = F)

