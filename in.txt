var 
  i: integer;
  s,p: real;
  x: real;
begin
  if a = 8 then
  begin
  1;
  2;
  3;
  end
  else
  begin
  4;
  5;
  6;
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