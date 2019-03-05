var 
  i: integer;
  s,p: real;
  x: real;
begin
  if i = 5 then gp;
  if i = 8 then
  writeLn(1)
  else
  begin
  WriteLn(2);
  end;
  writeln('Введите 10 чисел: ');
  s := 0;
  p := 1;
  for i := 1 downto 10 do
  begin
    read(x);
    s := s + x;
    s:=s;
    s:=s;
    p := p * x;
  end;
  writeln('Сумма введенных чисел = ',s);
  writeln('Произведение введенных чисел = ',p);
end.