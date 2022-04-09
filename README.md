http://www.faqs.org/faqs/msdos-programmer-faq/part2/section-5.html


http://c-faq.com/fp/fpnotlinked.html


> Some compilers for small machines, including Turbo C (and Ritchie's original PDP-11 compiler), leave out certain floating point support if it looks like it will not be needed. In particular, the non-floating-point versions of printf and scanf save space by not including code to handle %e, %f, and %g. It happens that Borland's heuristics for determining whether the program uses floating point are insufficient, and the programmer must sometimes insert a dummy call to a floating-point library function (such as sqrt; any will do) to force loading of floating-point support. (See the comp.os.msdos.programmer FAQ list for more information.)

> A partially-related problem, resulting in a similar error message (perhaps ``floating point not loaded'') can apparently occur under some MS-DOS compilers when an incorrect variant of the floating-point library is linked. Check your compiler manual's description of the various floating-point libraries.
