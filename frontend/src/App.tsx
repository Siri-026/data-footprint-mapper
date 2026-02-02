import { useState } from 'react';
import { useScan } from './hooks/useScan';
import type { ScanRequest } from './types/api.types';

function App() {
  const [identifier, setIdentifier] = useState('');
  const [identifierType, setIdentifierType] = useState<'email' | 'username'>('email');
  const { scan, loading, error, data, reset } = useScan();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const request: ScanRequest = {
      identifier,
      identifier_type: identifierType
    };
    scan(request);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold text-gray-900">
            🔍 My Data, Where Is It?
          </h1>
          <p className="text-gray-600 mt-1">
            Privacy-first personal data footprint scanner
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-4xl mx-auto px-4 py-12">
        {!data ? (
          /* Scan Form */
          <div className="bg-white rounded-2xl shadow-xl p-8">
            <div className="mb-6">
              <h2 className="text-2xl font-semibold text-gray-800 mb-2">
                Check Your Digital Footprint
              </h2>
              <p className="text-gray-600">
                Enter your email or username to see where your data might exist online
              </p>
            </div>

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Identifier Type
                </label>
                <select
                  value={identifierType}
                  onChange={(e) => setIdentifierType(e.target.value as 'email' | 'username')}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                  <option value="email">Email Address</option>
                  <option value="username">Username</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  {identifierType === 'email' ? 'Your Email' : 'Your Username'}
                </label>
                <input
                  type={identifierType === 'email' ? 'email' : 'text'}
                  value={identifier}
                  onChange={(e) => setIdentifier(e.target.value)}
                  placeholder={identifierType === 'email' ? 'name@example.com' : 'your_username'}
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  required
                />
              </div>

              {error && (
                <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
                  {error}
                </div>
              )}

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition-colors disabled:bg-gray-400 disabled:cursor-not-allowed"
              >
                {loading ? (
                  <span className="flex items-center justify-center">
                    <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    Scanning...
                  </span>
                ) : (
                  'Scan My Footprint'
                )}
              </button>
            </form>

            <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
              <p className="text-sm text-blue-800">
                🔒 <strong>Privacy First:</strong> We don't store your data. All scans are processed in real-time and never logged.
              </p>
            </div>
          </div>
        ) : (
          /* Results Dashboard */
          <div className="space-y-6">
            <div className="bg-white rounded-2xl shadow-xl p-8">
              <div className="flex justify-between items-start mb-6">
                <div>
                  <h2 className="text-2xl font-bold text-gray-900">Scan Results</h2>
                  <p className="text-gray-600 mt-1">for {identifier}</p>
                </div>
                <button
                  onClick={reset}
                  className="px-4 py-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                >
                  New Scan
                </button>
              </div>

              {/* Risk Score */}
              <div className="mb-8 p-6 bg-gradient-to-r from-blue-500 to-purple-600 rounded-xl text-white">
                <div className="text-sm font-medium mb-2">Exposure Score</div>
                <div className="text-5xl font-bold">{data.exposure_score.toFixed(1)}</div>
                <div className="text-sm mt-2 opacity-90">
                  Risk Level: <span className="font-semibold uppercase">{data.risk_level}</span>
                </div>
              </div>

              {/* Exposure Categories */}
              <div className="mb-8">
                <h3 className="text-xl font-semibold mb-4">Data Exposure Breakdown</h3>
                <div className="space-y-4">
                  {data.categories.map((category, idx) => (
                    <div key={idx} className="border border-gray-200 rounded-lg p-4">
                      <div className="flex justify-between items-start mb-2">
                        <h4 className="font-semibold text-gray-900">{category.name}</h4>
                        <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                          category.risk_level === 'high' ? 'bg-red-100 text-red-800' :
                          category.risk_level === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                          'bg-green-100 text-green-800'
                        }`}>
                          {category.risk_level}
                        </span>
                      </div>
                      <p className="text-gray-600 text-sm mb-3">{category.explanation}</p>
                      <div className="flex flex-wrap gap-2">
                        {category.platforms.map((platform, pidx) => (
                          <span key={pidx} className="px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded">
                            {platform}
                          </span>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Cleanup Plan */}
              {data.cleanup_plan.length > 0 && (
                <div>
                  <h3 className="text-xl font-semibold mb-4">Recommended Actions</h3>
                  <div className="space-y-3">
                    {data.cleanup_plan.map((action, idx) => (
                      <div key={idx} className="flex items-start gap-3 p-4 bg-gray-50 rounded-lg">
                        <div className="flex-shrink-0 w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold">
                          {action.priority}
                        </div>
                        <div className="flex-1">
                          <h4 className="font-medium text-gray-900">{action.action}</h4>
                          <p className="text-sm text-gray-600 mt-1">
                            Estimated time: {action.estimated_time}
                          </p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="mt-16 py-8 text-center text-gray-600 text-sm">
        <p>Built with privacy in mind • No data stored • Open source</p>
      </footer>
    </div>
  );
}

export default App;
