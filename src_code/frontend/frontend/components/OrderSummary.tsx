interface OrderSummaryProps {
  total: number;
}

const OrderSummary = ({ total }: OrderSummaryProps) => {
  return (
    <div>
      <h2>Order Summary</h2>
      <p>Total: {total}</p>
    </div>
  );
};

export default OrderSummary;