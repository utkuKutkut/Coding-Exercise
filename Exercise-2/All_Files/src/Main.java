import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class Main {

	public static void main(String[] args) throws InterruptedException, IOException {

		ConsumerProducer CP = new ConsumerProducer();

		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

		System.out.println("Input the m (Producer threads):");
		String mProducer = reader.readLine();
		System.out.println("Input the n (Consumer threads):");
		String nConsumer = reader.readLine();
		int n = Integer.parseInt(nConsumer);
		int m = Integer.parseInt(mProducer);

		while (m > 0 || n > 0) {

			Thread t1 = new Thread(new Runnable() {
				@Override
				public void run() {
					try {
						CP.producer();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			});
			Thread t2 = new Thread(new Runnable() {
				@Override
				public void run() {
					try {
						CP.consumer();
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			});

			if (m > 0) {
				t1.setName(String.valueOf(m));
				t1.start();
				m--;
			}
			if (n > 0) {
				t2.setName(String.valueOf(n));
				t2.start();
				n--;
			}

		}

	}

}
