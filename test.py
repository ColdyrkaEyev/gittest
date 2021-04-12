import cv2 
import argparse 


def main():
    parser = argparse.ArgumentParser(description="Display Image on the screen")
    parser.add_argument('image_path', type=str, help="Input path for Image")
    args = parser.parse_args()

    img = cv2.imread(args.image_path)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()