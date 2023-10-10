#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define MAXITERATION 255
#define k 3
#define w 1080*k        //Width of the image in pixel
#define h 720*k         //Height of the image in pixel

//Dimensions of the graph in the complex plane
#define Llimit -2
#define Rlimit  .5
#define Ulimit  -1
#define Dlimit  1

//n power of the z term
#define n 2


typedef struct complex{
    long double real;
    long double imag;
}complex;

complex csum(complex a, complex b){
    
    complex tmp = {a.real,a.imag};
    tmp.real += b.real;
    tmp.imag += b.imag;
    return tmp;

}

complex cprod(complex a, complex b){
    complex tmp = {((a.real*b.real)-(a.imag*b.imag)),((a.real*b.imag)+(b.real*a.imag))};
    return tmp;
}

complex c_pow(complex a, int pow){

    complex tmp ={a.real,a.imag};
    for(int i=1; i<pow; i++){
        tmp = cprod(tmp,tmp);
    }
    return tmp;
}

long double mod(complex z){
    return sqrt(pow(z.real,2)+pow(z.imag,2));
}

int bound(complex c){         //returns number of iterations necessary to diverge
    
    complex z = {0,0};
    int counter=0;

    for(int i=0;i<MAXITERATION; i++){
        
        z = c_pow(z,n);
        z = csum(z,c);
        if(mod(z) >= 2){
            return counter;
        }
        counter++;
    }
    return counter;
}


int** makeImg(long int Width,long int Height){

    int **canvas = (int**)malloc(sizeof(long int)* Width);

    for(long int j=0;j<Width;j++){
        canvas[j] = (int*)malloc(sizeof(int)*Height);
    }

    long double dx = ((long double)(Rlimit-Llimit))/(long double)Width;
    long double dy = ((long double)(Dlimit-Ulimit))/(long double)Height;

    for(long double i=Llimit; i<Rlimit; i += (dx)){
        for(long double j=Ulimit; j<Dlimit; j += (dy)){

            complex c = {i,j};
            canvas[(long int)((i-Llimit)/dx)][(long int)((j-Ulimit)/dy)] = bound(c);
        }
    }
    return canvas;
}

void prtImage(long int Width,long int Height, int** canvas){
    
    long int i,j=0;
    int temp =0;

    FILE* imgf;
    imgf = fopen("Mandelbrot_Set.png","wb");

    fprintf(imgf,"P2\n");
    fprintf(imgf, "%ld %ld\n", Width, Height);
    fprintf(imgf, "255\n");

    for (i = 0; i < Height; i++) { 
        for (j = 0; j < Width; j++) { 

            temp = canvas[j][i]; 
            fprintf(imgf, "%d ", temp); 
        
        }
        fprintf(imgf, "\n");
    } 
    fclose(imgf);
}


int main(){
    
    int **canvas = makeImg(w,h);
    __clock_t a = clock();
    prtImage(w,h,canvas);
    __clock_t b = clock();
    printf("Time : %f", (b-a)/CLOCKS_PER_SEC);

}