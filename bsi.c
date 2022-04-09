#include<stdio.h>
#include<conio.h>

struct student
{
    char name[20];
    char usn[20];
    float marks;
};

void main()
{
    struct student s[3];
    int i;
    clrscr();

    for(i = 0; i < 3; i++)
    {
        printf("Enter the details of student %d\n", i+1 );

        printf("Enter the name of the student\n");
        scanf("%s", s[i].name);

        printf("Enter the usn of the student\n");
        scanf("%s", s[i].usn);

        printf("Enter the marks of the student\n");
        scanf("%f", &s[i].marks);
    }

        printf("The student details are\n");
        printf("Name\tusn\t\t\tmarks\n");

    for(i = 0; i < 3; i++)
    {
        printf("%s\t%s\t\t%f\n", s[i].name,s[i].usn,s[i].marks );
    }

    getch();
}
