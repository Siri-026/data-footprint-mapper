import { useState } from 'react';
import type { ScanRequest } from '../types/api.types';

interface Props {
  onScan: (req: ScanRequest) => void;
  loading: boolean;
}

export const ScanForm = ({ onScan, loading }: Props) => {
  const [identifier, setIdentifier] = useState('');
  const [type, setType] = useState<'email' | 'username'>('email');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onScan({ identifier, identifier_type: type });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-4">My Data, Where Is It?</h1>
      <p className="text-gray-600 mb-6">
        Check where your personal data might exist online
      </p>
      
      <input
        type="text"
        value={identifier}
        onChange={(e) => setIdentifier(e.target.value)}
        placeholder="Enter email or username"
        className="w-full p-3 border rounded mb-4"
        required
      />
      
      <select
        value={type}
        onChange={(e) => setType(e.target.value as any)}
        className="w-full p-3 border rounded mb-4"
      >
        <option value="email">Email Address</option>
        <option value="username">Username</option>
      </select>
      
      <button
        type="submit"
        disabled={loading}
        className="w-full bg-blue-600 text-white p-3 rounded hover:bg-blue-700 disabled:bg-gray-400"
      >
        {loading ? 'Scanning...' : 'Scan My Footprint'}
      </button>
    </form>
  );
};
