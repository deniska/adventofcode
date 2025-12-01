var
    infile: text;
    p1, p2, q, i, n, dir: integer;
    d: char;
begin
    if ParamCount < 1 then begin
        writeln('Please filename');
        halt(1);
    end;

    assign(infile, ParamStr(1));
    reset(infile);

    p1 := 0;
    p2 := 0;
    q := 50;

    while not eof(infile) do begin
        read(infile, d, n);
        readln(infile);
        if d = 'R' then dir := 1 else dir := -1;
        for i := 1 to n do begin
            q := (q + dir) mod 100;
            if q = 0 then inc(p2);
        end;
        if q = 0 then inc(p1);
    end;

    writeln(p1);
    writeln(p2);
end.
