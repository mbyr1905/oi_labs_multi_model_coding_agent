import { useRouter } from 'next/router';
import ProductCard from '../../components/ProductCard';

const ProductDetailPage = () => {
    const router = useRouter();
    const { id } = router.query;

    const product = { id: 1, title: 'Product 1', description: 'Description 1', price: 10.99, image: 'image1.jpg' };

    return (
        <div>
            <h1>Product Detail Page</h1>
            <ProductCard product={product} />
        </div>
    );
};

export default ProductDetailPage;