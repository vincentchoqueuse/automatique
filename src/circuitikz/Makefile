# Directory to place PNG files
PNG_DIR = ../../content/course/img

# Find all .tex files in the current directory
TEX_FILES := $(wildcard *.tex)

# Convert .tex filenames to .pdf and .png filenames
PDF_FILES := $(TEX_FILES:.tex=.pdf)
PNG_FILES := $(addprefix $(PNG_DIR)/, $(TEX_FILES:.tex=.png))

# Default target
all: $(PNG_FILES)

# Rule to convert .tex to .pdf
%.pdf: %.tex
	pdflatex $<

# Rule to convert .pdf to .png and place in the PNG_DIR
$(PNG_DIR)/%.png: %.pdf | $(PNG_DIR)
	convert -density 500 $< -quality 90 -background white -alpha remove -alpha off $@

# Create the PNG_DIR if it doesn't exist
$(PNG_DIR):
	mkdir -p $@

# Clean up generated files
clean:
	rm -f *.pdf *.aux *.log $(PNG_DIR)/*.png

.PHONY: all clean
