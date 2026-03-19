import Link from 'next/link';

interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

const ProductCard = ({ product }: { product: Product }) => {
  return (
    <div>
      <h2>{product.name}</h2>
      <p>{product.description}</p>
      <p>Price: {product.price}</p>
      <Link href={`/product/${product.id}`}>View Details</Link>
    </div>
  );
};

export default ProductCard;