using MLDatasets, Flux
using Flux:onehotbatch,crossentropy,@epochs,train!,throttle,mean,onecold

train_x = reshape(MNIST.traintensor(), (784, 60000))
train_y = onehotbatch(MNIST.trainlabels(), 0:9)
test_x = reshape(MNIST.testtensor(), (784, 10000))
test_y = onehotbatch(MNIST.testlabels(), 0:9)

model = Chain(
    Dense(784, 256, relu),
    Dense(256, 128, relu),
    Dense(128, 10),
    softmax
)

loss(X, y) = crossentropy(model(X), y)
optim = ADAM()
progress = () -> @show(loss(train_x, train_y))

@epochs 100 train!(loss, params(model), [(train_x, train_y)], optim, cb = throttle(progress, 10))

accuracy(X, y) = mean(onecold(model(X)) .== onecold(y))
println("Training accuracy: $(accuracy(train_x, train_y))")
println("Test accuracy: $(accuracy(test_x, test_y))")
