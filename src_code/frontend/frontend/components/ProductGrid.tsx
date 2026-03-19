import ProductCard from './ProductCard';

interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

const ProductGrid = ({ products }: { products: Product[] }) => {
  return (
    <div>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

export default ProductGrid;