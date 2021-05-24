Ts = 1/100;

x = -1:Ts:1;
y = -1:Ts:1;
L = length(x);
for i = 1:length(x)
    y(i) = abs(x(i)) - 1;
end


f = fft(x);
fs = 1/Ts;
freq = (0:length(f)-1)*fs/length(f);
plot(freq, abs(f))
 