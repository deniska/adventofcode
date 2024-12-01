Procedure SortArray(a) // you live like that?
    ValueList = New ValueList;
    ValueList.LoadValues(a);
    ValueList.SortByValue();
    a = ValueList.UnloadValues(); 
EndProcedure;

Numbers1 = New Array;
Numbers2 = New Array;
Counts = New Map;

Text = New TextReader;
Text.Open(CommandLineArguments[0]);
Line = Text.ReadLine();
While Line <> Undefined Do
    Elements = StrSplit(Line, " ", False);
    If Elements.Count() = 0 Then Continue; EndIf;
    Numbers1.Add(Number(Elements[0]));
    Numbers2.Add(Number(Elements[1]));
    c = Counts.Get(Number(Elements[1]));
    Counts.Insert(Number(Elements[1]), ?(c = Undefined, 0, c) + 1);
    Line = Text.ReadLine();
EndDo;

SortArray(Numbers1);
SortArray(Numbers2);

Count = Numbers1.Count();
Result1 = 0;
Result2 = 0;

For i = 0 To Count - 1 Do
    n = Numbers1[i] - Numbers2[i];
    Result1 = Result1 + ?(n >= 0, n, -n);
    c = Counts.Get(Numbers1[i]);
    Result2 = Result2 + Numbers1[i] * ?(c = Undefined, 0, c);
EndDo;

Message(Result1);
Message(Result2);
