# Gaziantep Local RAG Project

Bu proje, yerel kaynaklar (belgeler, metinler vb.) üzerine kurulu, harici bir API anahtarına ihtiyaç duymadan tamamen lokalde (bilgisayar üzerinde) çalışan bir *RAG (Retrieval-Augmented Generation)* sistemidir.

## Projenin Amacı
Sistem, docs klasörünün içerisinde bulunan belgeleri tarayarak kullanıcıların sorularına en doğru, belgelerle desteklenen ve bağlamsal yanıtlar üretmeyi amaçlar.

## Proje Yapısı
* main.py: Projenin ana çalıştırma dosyası ve RAG akışının yönetildiği betik.
* docs/: Projenin bilgi dağarcığını oluşturan kaynak belgelerin bulunduğu klasör.

## Gereksinimler
Projeyi çalıştırmak için bilgisayarınızda şu araçların kurulu olması gerekmektedir:
* Python
* Ollama (Lokal dil modeli için)

## Nasıl Çalıştırılır?
1. Projeyi bilgisayarınıza klonlayın veya indirin.
2. Terminal üzerinden proje klasörüne gidin.
3. Ana betiği çalıştırmak için şu komutu girin:
   ```bash
   python main.py
