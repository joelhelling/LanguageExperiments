def main():
	pythag = [];
	product = 0;
	for i in range(3,1000):
		for j in range(i,1000):
			for k in range(j,1000):
				if i*i + j*j == k*k:
					pythag.append((i,j,k));
					if (i + j + k) == 1000:
						product = i * j * k;
						print("found " , i, j, k);

	print(pythag);
	print(product);

main();