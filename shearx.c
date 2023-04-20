#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i,n;
    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    int x[n], y[n];
    for(i=0;i<n;i++)
	 {
        printf("Enter x and y coordinates of vertex %d: ", i+1);
        scanf("%d %d", &x[i], &y[i]);
     }
    float shearFactor;
    printf("Enter the shear factor: ");
    scanf("%f", &shearFactor);
    printf("Original Polygon:\n");
    for(i=0;i<n;i++)
	 {
        printf("(%d,%d) ", x[i], y[i]);
     }
    for(i=0;i<n;i++)
	 {
        x[i] = x[i] + shearFactor * y[i];
     }
    printf("\nSheared Polygon:\n");
    for(i=0;i<n;i++)
	 {
        printf("(%d,%d) ", x[i], y[i]);
     }

    return 0;
}

