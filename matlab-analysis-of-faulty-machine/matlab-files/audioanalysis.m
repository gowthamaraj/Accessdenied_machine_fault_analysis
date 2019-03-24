
whaleFile = '.\bluewhale.mp3';
[x,fs] = audioread(whaleFile);
%subplot(2,1,1)
plot(x);
xlabel('Sample Number')
ylabel('Amplitude')
moan = x(2.45e4:3.10e4);
t = 10*(0:1/fs:(length(moan)-1)/fs);

max(moan)
plot(t,moan)
xlabel('Time (seconds)')
ylabel('Amplitude')
xlim([0 t(end)])
m = length(moan);       % original sample length
n = pow2(nextpow2(m));  % transform length
y = fft(moan,n);        % DFT of signal
f = (0:n-1)*(fs/n)/10;
power = abs(y).^2/n;      

figure(1)
plot(f(1:floor(n/2)),power(1:floor(n/2)))

xlabel('Frequency')
ylabel('Power')
