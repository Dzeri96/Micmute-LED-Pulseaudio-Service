#include <stdio.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

const char *BRIGHTNESS_FILE_PATH = "/sys/class/leds/platform::micmute/brightness";

int main(int argc, char *argv[]) {

    long newval;
    FILE *fp;

    if(argc != 2 || (strlen(argv[1]) == 0) ||(strspn(argv[1],"0123456789") != strlen(argv[1]))) {
        fprintf(stderr, "Value not supplied!\n");
        exit(22);
    }

    errno = 0;
    newval = strtol(argv[1], NULL, 10);
    /* Check for various possible errors */
    if ((errno == ERANGE && (newval == LONG_MAX || newval == LONG_MIN))
            || (errno != 0 && newval == 0) || (newval != 0 && newval != 1)) {
        fprintf(stderr, "Error parsing input!\n");
        exit(EXIT_FAILURE);
    }

    fp = fopen(BRIGHTNESS_FILE_PATH, "w");
    if(fp != NULL) {
        fprintf(fp, "%ld", newval);
    } else {
        fprintf(stderr, "Error when opening file: %s\n", strerror(errno));
    }
    fclose(fp);

}