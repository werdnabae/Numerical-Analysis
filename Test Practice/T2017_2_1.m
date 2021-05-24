% x = 1:5;
% x = transpose(x);
% y = [5521.06, 5574.12, 5555.33, 5660.78, 5666.77];
% y = transpose(y);
% 
% f = fit(x, y, 'poly4');
% g = fit(x, y, 'poly1');
% disp(f);
% disp(g);
% plot(f, x, y);
% hold on
% plot(g, 'g');
% legend('points', '4th', '1st', 'Location', 'northwest');

x1 = 0.1:0.1:0.5;
x1 = transpose(x1);
y1 = [1.1141842615436537, 1.2637194336484336, 1.455997623426589, 1.7006938833473375, 2.0104749566723124];
y1 = transpose(y1);
f = fit(x1, y1, 'poly4');