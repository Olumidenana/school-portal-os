export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');

  if (req.method === 'OPTIONS') {
    res.status(200).end();
    return;
  }

  const publicKey = process.env.PAYSTACK_PUBLIC_KEY || 
                    process.env.NEXT_PUBLIC_PAYSTACK_KEY || 
                    process.env.PAYSTACK_KEY || 
                    '';

  const mode = publicKey.startsWith('pk_live_') ? 'live' : (publicKey.startsWith('pk_test_') ? 'test' : 'demo');

  res.status(200).json({
    paystackPublicKey: publicKey,
    mode: mode
  });
}
