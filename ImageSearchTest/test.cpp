#include "pch.h"
#include "../ImageSearchDLL/util.h"

TEST(TestImageSearch, ImageSearch) {
	char *ret = ImageSearch(0, 0, 10, 10, 0, "..\\Test\\test1.bmp");
	EXPECT_TRUE(strcmp(ret, "0") != 0);
}

TEST(TestImageSearch, ImageSearchWrongImage) {
	char *ret = ImageSearch(0, 0, 10, 10, 2, "..\\Test\\test2.bmp");
	EXPECT_TRUE(strcmp(ret, "0") == 0);
}

TEST(TestImageSearch, ImageSearchFixWrongImage) {
	char *ret = ImageSearch(0, 0, 10, 10, 3, "..\\Test\\test2.bmp");
	EXPECT_TRUE(strcmp(ret, "0") != 0);
}