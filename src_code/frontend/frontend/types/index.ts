export interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
}

export interface Category {
  id: number;
  name: string;
}

export interface CartItem {
  id: number;
  name: string;
  price: number;
}

export interface Order {
  id: number;
  total: number;
}