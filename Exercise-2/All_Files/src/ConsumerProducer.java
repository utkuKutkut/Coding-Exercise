import java.util.ArrayList;
import java.util.List;

public class ConsumerProducer {
	List<Integer> buffer = new ArrayList<Integer>();
	int capacity = 5;
	volatile int index = 0;

	public void producer() throws InterruptedException {
		int num = 1;
		while (true) {
			synchronized (this) {
				while (index == capacity) {
					wait();
					System.out.println("Producer " + Thread.currentThread().getName() + " took the lock!");
				}

				System.out.println("Producer " + Thread.currentThread().getName() + " produced: " + num);
				buffer.add(index, num);
				;
				num++;
				index++;
				notify();

			}
		}
	}

	public void consumer() throws InterruptedException {
		while (true) {
			synchronized (this) {
				while (buffer.size() == 0) {
					wait();
				}

				int val = buffer.get(0);
				buffer.remove(--index);
				System.out.println("Consumer " + Thread.currentThread().getName() + " consumed:" + val);

				notify();

			}
		}
	}

}
