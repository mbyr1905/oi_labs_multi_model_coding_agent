import type { Order } from '../types';

const OrderSummary = ({ order }: { order: Order }) => {
  return (
    <div>
      <h2>Order Summary</h2>
      <p>Total: {order.total}</p>
    </div>
  );
};

export default OrderSummary;