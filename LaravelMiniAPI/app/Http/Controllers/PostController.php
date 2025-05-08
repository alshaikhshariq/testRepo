<?php

namespace App\Http\Controllers;

use App\Http\Requests\StorePostRequest;
use App\Http\Resources\PostResource;
use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\AnonymousResourceCollection;

class PostController extends Controller
{
    public function store(StorePostRequest $request): PostResource
    {
        $post = $request->user()->posts()->create([
            ...$request->validated(),
            'posted_at' => now()
        ]);
        return new PostResource($post);
    }

    public function index(Request $request): AnonymousResourceCollection
    {
        $query = $request->user()->posts()->latest('posted_at');
        if ($request->has('platform')) {
            $query->where('platform', $request->platform);
        }
        return PostResource::collection($query->paginate(10));
    }

}
