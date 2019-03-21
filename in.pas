begin
function 4(a,b,c);
begin
123
end;

var
  i: integer;
  s,p: real;
  x: real;


begin
  for a:=6 to 10 do for c:=9 to 19 do helloWorld;
  if i = 8 then
  writeLn(1)
  else
  begin
  WriteLn(2);
  end;
  writeln('Введите 10 чисел: ');
  s := 0;
  p := 1;
  for i := 1 downto 10 step 5 do
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