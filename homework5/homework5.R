library("GEOquery")
library(pheatmap)
library(ggplot2)
library(ggrepel)
library(limma)
library(ggrepel)
library(dplyr)
library(ReactomePA)
library(DOSE)


#1. Differential gene expression analysis is among the most fundamental analyses in modern bioinformatics. Use appropriate R packages to accomplish the following objectives.
#a.Download ‘GSE33126’ from Gene Expression Omnibus
my_id <- "GSE33126"
gse <- getGEO(my_id)

#b.Print the expression levels present in the data
gse <- gse[[1]]
expression_data <- exprs(gse)
print(expression_data)

#c.Log-normalize the data
log_exp <- log2(expression_data)

#d.Create box-plot illustrating your the log-normalized data
boxplot(log_exp,outline=FALSE)

#e.Load the corresponding phenotype data and print it
phenotype_data <- pData(gse)
print(phenotype_data)

#f.Perform clustering between your samples and display it as a heat map
corMatrix <- cor(log_exp,use="c")
pheatmap(corMatrix)

#g.Recreate the heat map from part e, including annotations for the patient id as well as patient group
pheno1 <- dplyr::select(phenotype_data, source_name_ch1,characteristics_ch1.1)
colnames(pheno1) <- c("Group", "Patient")
rownames(pheno1) <- colnames(corMatrix)
pheatmap(corMatrix,annotation_col=pheno1)

#h.Create a scatter plot of your data utilizing Principle Component Analysis (PCA) vectors
pca <- prcomp(t(log_exp))
## Join the PCs to the sample information
cbind(pheno1, pca$x) %>%
  ggplot(aes(x = PC1, y=PC2, col=Group,label=Patient)) + geom_point() + geom_text_repel()


#i.Identify a list of Differentially Expressed Genes (DEGs), print them, along with associated p-value and their adjusted p-value
design <- model.matrix(~0+pheno1$Group)
colnames(design) <- c("Normal","Tumor") #rename
fit <- lmFit(log_exp, design)
contrasts <- makeContrasts(Tumor - Normal, levels=design)
fit2 <- contrasts.fit(fit, contrasts)
fit2 <- eBayes(fit2)
anno <- fData(gse)
anno <- dplyr::select(anno,Symbol,Entrez_Gene_ID)
fit2$genes <- anno
full_results <- topTable(fit2, number=Inf)
full_results <- tibble::rownames_to_column(full_results,"ID")
full_results <- full_results[!duplicated(full_results$Entrez_Gene_ID),]
head(full_results)
p_cutoff <- 0.05
fc_cutoff <- 1
topN<-20
DEG_results <- full_results[full_results$adj.P.Val < p_cutoff & abs(full_results$logFC)>fc_cutoff, ]
head(DEG_results)


#j.Create a volcano plot displaying all of the measured genes, highlight the DEGs with a different color
full_results %>%
  mutate(Significant = adj.P.Val < p_cutoff, abs(logFC) > fc_cutoff ) %>%
  ggplot(aes(x = logFC, y = B, col=Significant)) + geom_point()

#k.Create an MA plot displaying all fo the measured genes, highlight the DEGs with a different color
full_results %>%
  mutate(Significant = adj.P.Val < p_cutoff, abs(logFC) > fc_cutoff ) %>%
  ggplot(aes(x = AveExpr, y = logFC, col=Significant)) + geom_point()

#l.Use the identified DEGs to determine over-represented Reactome pathways
de <- DEG_results$Entrez_Gene_ID
enrich_result <- enrichPathway(gene=de, pvalueCutoff = 0.05, readable=TRUE)
head(enrich_result)
summary(enrich_result)


#m.Perform Gene Set Enrichment analysis on your identified DEGs
genelist <- as.vector(DEG_results$logFC)
genelist <- setNames(genelist, DEG_results$Entrez_Gene_ID)
genelist <- sort(genelist, decreasing = TRUE)
GSEA <- gsePathway(genelist,
                pvalueCutoff = 0.05,
                pAdjustMethod = "BH",
                verbose = FALSE)
head(GSEA)

#n.Visualize your pathway as a network
#Select one of the pathway descriptions from your over-represented Reactome Pathways from part l, as the primary input.
viewPathway("Chemokine receptors bind chemokines",
            readable = TRUE,
            foldChange = genelist)


#o.Perform Disease Gene Set Enrichment analysis using your identified DEGs
DGSE <- gseDO(genelist,
           minGSSize     = 100,
           pvalueCutoff  = 0.05,
           pAdjustMethod = "BH",
           verbose       = FALSE)
head(DGSE, 3)
