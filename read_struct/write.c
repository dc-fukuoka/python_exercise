#include <stdio.h>

typedef struct test_t {
	unsigned int u[2];
	long         l;
	char         str[8];
} test_t;

int main(int argc, char **argv)
{
	FILE *fp;
	test_t test = {
		.u = {1, 2},
		.l = 15,
		.str = "test",
	};
	fp = fopen("./test.dat", "wb");
	fwrite(&test, sizeof(test), 1, fp);
	fclose(fp);
	
	return 0;
}
