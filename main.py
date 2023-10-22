from ThresholdFilter import ThresholdFilter

def main():
    print("test")
    filter = ThresholdFilter()
    filter.loadImage();
    filter.blurImage();
    filter.thresholdFilter();
    #show things
    filter.showBinaryMask();
    filter.createHistogram();

if __name__ == "__main__":
    main()
