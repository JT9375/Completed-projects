%{
  #include <stdio.h>
  #include "boolcalc.tab.h"
%}
%option noyywrap

%%

[ \t]	;
["T"|"t"]["R"|"r"]["U"|"u"]["E"|"e"]		{yylval = 1; return NUM;}
["F"|"f"]["A"|"a"]["L"|"l"]["S"|"s"]["E"|"e"]	{yylval = 0; return NUM;}
\n						{return NEWLINE;}
"&"						{return AND;}
"|"						{return OR;}
"'"						{return NOT;}

%%
